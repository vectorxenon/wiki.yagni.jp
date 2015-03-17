# Activity開始時にIMEを起動しないようにする

レイアウトの中にEditTextを設置すると、Activityを起動した時にソフトキーボードが起動してしまう。
これを制御するにはInputMethodManagerを使ったり、見えないEditTextを用意したりするが、一番簡単なのは_Window#setSoftInputMode()_を使う方法。

```java
public class FooActivity extends Activity
{
    @Override
    public void onCreate(Bundle SavedInstanceState)
    {
        super.onCreate(SavedInstanceState);
        getWindow().setSoftInputMode(LayoutParams.SOFT_INPUT_STATE_HIDDEN);
        setContentView(R.layout.main);
    }
}
```
