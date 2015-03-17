# ListViewでクリックできない場合の対処法

ListViewをカスタマイズした時に、行の中にCheckBoxを置くとOnItemClickイベントが効かなくなる。
これはCheckBoxがフォーカスを奪ってしまい、ListViewにフォーカスしなくなる。

なので原因となっているもののフォーカスを無効にすると解決する。

```xml
<CheckBox android:focusable="false" />
```
