# LinearLayoutを利用して2つのウィジェットを中央寄せする

```xml
<LinearLayout android:id="@+id/buttons"
    android:orientation="horizontal"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
>
    <Button android:id="@+id/ok"
        android:text="OK"
        android:layout_width="0dp"
        android:layout_height="match_parent"
        android:layout_weight="1"
        android:singleLine="true"
    />
    <Button android:id="@+id/cancel"
        android:text="Cancel"
        android:layout_width="0dp"
        android:layout_height="match_parent"
        android:layout_weight="1"
        android:singleLine="true"
    />
</LinearLayout>
```
