# SDカード上にファイルを保存する

## メディアディレクトリに画像を保存する

```java
Uri savedUri = Uri.parse(MediaStore.Images.Media.insertImage(context.getContentResolver(),
        bitmap, "title", "description");
```
