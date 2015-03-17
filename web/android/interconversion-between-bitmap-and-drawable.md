# BitmapとDrawableの相互変換

## DrawableからBitmapへの変換

```java
((BitmapDrawable)drawable).getBitmap()
```

## BitmapからDrawableへの変換

```java
new BitmapDrawable(bitmap)
```
