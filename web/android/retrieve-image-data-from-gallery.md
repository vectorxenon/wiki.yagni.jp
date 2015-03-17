# ギャラリーなどから選択した画像を受け取る

カメラで撮影したものは3000x4000などの解像度が大きいものが多いので、そのまま読み込むとメモリが溢れてしまう。\\
なので、先に画像の縦横サイズを取得し、使用するサイズにリサイズしてから受け取るようにする。

画像の情報だけを取得するには、_BitmapFactory.decodeStream()_のオプションで_inJustDecodeBounds_をtrueにすると実現できる。

以下は選択された画像をアイコンのサイズにリサイズしている。

```java
Bitmap bitmap = null;
Uri photoUri = data.getData();
if (photoUri == null) {
    bitmap = data.getParcelableExtra("data");
} else {
    InputStream is = null;
    BitmapFactory.Options options = null;
    try {
        // 画像の情報だけを取得する
        is = getContentResolver().openInputStream(photoUri);
        options = new BitmapFactory.Options();
        options.inJustDecodeBounds = true;
        BitmapFactory.decodeStream(is, null, options);
    } catch (IOException e) {
        Log.d(TAG, "Selected picture can't retrieve infomation: " + e.getLocalizedMessage());
    } finally {
        try {
            is.close();
        } catch (Exception e) {
        }
    }
    try {
        BitmapFactory.Options options2 = new BitmapFactory.Options();
        int width = getResources().getDimensionPixelOffset(android.R.dimen.app_icon_size);
        float outWidth = options.outWidth;
        int scale = (int)(outWidth / width);
        options2.inSampleSize = scale;
        is = getContentResolver().openInputStream(photoUri);
        bitmap = BitmapFactory.decodeStream(is, null, options2);
    } catch (FileNotFoundException e) {
        Log.d(TAG, "Picture not found: " + e.getLocalizedMessage());
    } finally {
        try {
            is.close();
        } catch (Exception e) {
        }
    }
}
```
