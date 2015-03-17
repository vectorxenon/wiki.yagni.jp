# SDカードの状態を調べる

```java
String status = Environment.getExternalStorageState();

if (status.equals(Environment.MEDIA_MOUNTED)) {
    //読み書きが可能
} else if (status.equals(Environment.MEDIA_MOUNTED_READ_ONLY)) {
    // 読み取り専用
} else if (status.equals(Environment.MEDIA_REMOVED)) {
    // SDカードが装着されていない
} else if (status.equals(Environment.MEDIA_SHARED)) {
    // マウント中
} else if (status.equals(Environment.MEDIA_BAD_REMOVAL)) {
    // アンマウントする前に取り外した
} else if (status.equals(Environment.MEDIA_CHECKING)) {
    // SDカードのチェック中
} else if (status.equals(Environment.MEDIA_NOFS)) {
    // 要フォーマット
} else if (status.equals(Environment.MEDIA_UNMOUNTABLE)) {
    // マウントすることができない
} else if (status.equals(Environment.MEDIA_UNMOUNTED)) {
    // アンマウントされた
} else {
    // その他の要因で利用不可能
}
```
