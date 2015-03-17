# 範囲選択した画像を取得する

ギャラリーで画像を選択させて、その画像を範囲選択させる機能を実行させる。

```java
// some onclick
float width, height;
width = height = activity.getResources().getDimension(android.R.dimen.app_icon_size);
intent = new Intent(Intent.ACTION_GET_CONTENT);
intent.setType("image/*");
intent.putExtra("crop", "true");
intent.putExtra("outputX", width);
intent.putExtra("outputY", height);
intent.putExtra("aspectX", width);
intent.putExtra("aspectY", height);
intent.putExtra("noFaceDetection", true);
intent.putExtra("return-data", true);
activity.startActivityForResult(intent, SOME_REQ_ID);
```

画像の受け取り方は[こちら](retrieve-image-data-from-gallery.md)
