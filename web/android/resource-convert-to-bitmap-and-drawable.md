# ResourceからBitmapおよびDrawableへの変換

## Bitmap -> Drawable

```java
BitmapFactory.decodeResource(context.getResources(), R.drawable.icon)
```

## Drawable -> Bitmap

```java
context.getResource().getDrawable(R.drawable.icon)
```
