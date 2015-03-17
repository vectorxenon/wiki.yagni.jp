# ディスプレイサイズを取得する

Contextから取得可能

```java
Display display = context.getWindowManager().getDefaultDisplay();
int width = display.getWidth();
int height = display.getHeight();
```
