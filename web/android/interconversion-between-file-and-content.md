# contentスキーマとfileスキーマの相互変換

## contentからfileへの変換

```java
Cursor c = getContentResolver().query(uri, null, null, null, null);
c.moveToFirst();
String filename = c.getString(c.getColumnIndex(MediaStore.MediaColumns.DATA));
```

## fileからcontentへの変換

```java
Cursor c = getContentResolver().query(MediaStore.Images.Media.EXTERNAL_CONTENT_URI,
        null,
        MediaStore.Images.ImageColumns.DATA + " = ?",
        new String[]{filename}, null);
c.moveToFirst();
String contentname = "content://media/external/images/media/" +
        c.getInt(c.getColumnIndex(MediaStore.MediaColumns._ID));
```
