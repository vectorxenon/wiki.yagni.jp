# Bitmapとbyte[]の相互変換

## Bitmapからbyte[]への変換

```java
ByteArrayOutputStream os = new ByteArrayOutputStream();
bitmap.compress(CompressFormat.JPEG, 100, os);
byte[] bin = os.toByteArray();
```

## byte[]からBitmapへの変換

```java
BitmapFactory.Options options = new BitmapFactory.Options();
Bitmap bitmap = BitmapFactory.decodeByteArray(bin, 0, bin.length, options);
```
