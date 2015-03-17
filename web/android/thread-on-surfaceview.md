# SurfaceViewにおけるスレッドの取り扱い方法

サンプルのLunar Landerのソースだと次のようにSurfaceView上でThreadをスタートさせている。

```java
@Override
public void surfaceCreated(SurfaceHolder holder)
{
    thread.setRunning(true);
    thread.start();
}
```

このままだとゲーム画面から別のアクティビティに飛ばして戻ってきたときに、IllegalThreadStateExceptionが起きてしまう。
なので次のように組む。

```java
@Override
public void surfaceCreated(SurfaceHolder holder)
{
    if (thread.getState() == Thread.State.TERMINATED) {
        thread = new FooThread();
    }
    thread.setRunning(true);
    thread.start();
}
```

## 参考

  * [android - IllegalThreadStateException in Lunarlander (or SurfaceView?)](http://code.google.com/p/android/issues/detail?id=972)
  * [Returning to SurfaceView after another Activity has taken focus - Stack Overflow](http://stackoverflow.com/questions/3893633/returning-to-surfaceview-after-another-activity-has-taken-focus)
  * [Wonton Games: Tutorial: Lunar Lander Resume Game Workaround](http://wonton-games.blogspot.com/2010/06/lunar-lander-resume-game-workaround.html)
