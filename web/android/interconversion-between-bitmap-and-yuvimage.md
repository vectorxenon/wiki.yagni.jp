# YUVな画像からRGBな画像への変換

```java
byte[] yuvData;
YuvImage yuvImage = new YuvImage(yuvData, ImageFormat.NV21, width, height, null);
ByteArrayOutputStream baos = new ByteArrayOutputStream();
int quality = 100;
yuvImage.compressToJpeg(new Rect(0, 0, width, height), quality, baos);
byte[] rgbData = baos.toByteArray();
```
