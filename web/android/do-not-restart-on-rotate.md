# 画面回転時にActivityを再起動させない

Androidでは画面を回転させた時にActivityが再起動される仕様になっている。
何かの入力系を実装する場合、再起動されてしまうと今まで入力していた内容が消えてしまうので、ユーザにとっては不便なものになってしまう。

これを制御するにはActivity毎に環境設定の変更に対してイベントを受信できる仕組みが用意されているので、それを利用する。

## Manifestへの追加

まずはイベントを受信するようにManifestファイルの<activityに設定を追加する。

```xml
<activity android:name=".FooActivity"
    android:label="@string/app_name"
    android:screenOrientation="sensor"
    android:configChanges="keyboardHidden|orientation"
>
```

keyboardHiddenはハードキーボード関連っぽいので、回転だけならorientationだけでよい。
しかしkeyboardHidden|orientationをイディオムとして覚えておいたほうがいいと思う。

## onConfigurationChanged()の処理

何かレイアウトの中のデータを変更したい場合は適時処理を実装する。
今回は再起動を止めるだけなので、何もしない。

```java
@Override
public void onConfigurationChanged(Configuration newConfig)
{
    super.onConfigurationChanged(newConfig);
}
```

## 参考

  * [&lt;activity&gt; - ソフトウェア技術ドキュメントを勝手に翻訳](http://www.techdoctranslator.com/android/guide/manifest/activity-element#config)
  * [7.3 実行時の変化への対処 - ソフトウェア技術ドキュメントを勝手に翻訳](http://www.techdoctranslator.com/android/guide/resources/runtime-changes)
