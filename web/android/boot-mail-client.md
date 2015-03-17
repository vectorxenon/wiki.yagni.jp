# メールクライアントを起動させる

## テキストのみ

mailtoスキームのUriにも件名と内容を入れないと、K-9 mailなどがEXTRA_SUBJECTとEXTRA_TEXTに対応していないのでうまくいかない。

```java
Intent intent = new Intent(Intent.Action_SENDTO);
intent.setData(Uri.parse("mailto:foo@bar?subject=SomeSubject&body=SomeBody"));
intent.putExtra(Intent.EXTRA_SUBJECT, "SomeSubject");
intent.putExtra(Intent.EXTRA_TEXT, "SomeBody");
Intent.createChooser(intent, "Choose an operation");
```

## 添付ファイルをつける

EXTRA_STREMに添付ファイルへのUriをセットする。
スキーマは_content_と_file_のどちらでも大丈夫。

```java
Intent intent = new Intent(Intent.Action_SEND);
intent.putExtra(Intent.EXTRA_EMAIL, "foo@bar");
intent.putExtra(Intent.EXTRA_SUBJECT, "SomeSubject");
intent.putExtra(Intent.EXTRA_TEXT, "SomeBody");
intent.setType("plain/text");
intent.putExtra(Intent.EXTRA_STREAM, Uri.parse("content://media/123"));
Intent.createChooser(intent, "Choose an operation");
```

## 複数の添付ファイルをつける

```java
Intent intent = new Intent(Intent.Action_SEND_MULTIPLE);
intent.putExtra(Intent.EXTRA_EMAIL, "foo@bar");
intent.putExtra(Intent.EXTRA_SUBJECT, "SomeSubject");
intent.putExtra(Intent.EXTRA_TEXT, "SomeBody");
intent.setType("plain/text");
List<Uri> list = new ArrayList<Uri>(){{
    add(Uri.parse("content://media/123"));
    add(Uri.parse("content://media/456"));
    add(Uri.parse("content://media/789"));
}};
intent.putExtra(Intent.EXTRA_STREAM, list);
Intent.createChooser(intent, "Choose an operation");
```
