# 画面の向きを取得する

```java
int orientation = context.getResources().getConfiguration().orientation
```

返ってくる値は_Configuration_に定義されているフラグ

```java
switch (orientation) {
case Configuration.ORIENTATION_LANDSCAPE:
    Log.d(TAG, "横");
    break;
case Configuration.ORIENTATION_PORTRAIT:
    Log.d(TAG, "縦");
    break;
default:
    Log.d(TAG, "その他");
    break;
}
```

## 参考

[Configuration | Android Developers](http://developer.android.com/intl/ja/reference/android/content/res/Configuration.html)
