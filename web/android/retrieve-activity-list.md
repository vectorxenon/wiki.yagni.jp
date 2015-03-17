# Activityの一覧を取得する

## ResolveInfoの取得

```java
List<ActivityInfo> activityInfoList = new ArrayList<ActivityInfo>();
PackageManager pm = context.getPackageManager();
Intent queryIntent = new Intent(Intent.ACTION_MAIN);
queryIntent.addCategory(Intent.CATEGORY_LAUNCHER);
List<ResolveInfo> resolveInfoList = pm.queryIntentActivities(queryIntent, PackageManager.MATCH_DEFAULT_ONLY);
for (ResolveInfo resolveInfo: resolveInfoList) {
    activityInfoList.add(resolveInfo.activityInfo);
}
```

## Intentの作成

Intentを作るにはActivityInfo#packageNameとActivityInfo#nameを使う。

```java
ActivityInfo activityInfo = resolveInfo.activityInfo;
Intent intent = new Intent(activityInfo.packageName, activityInfo.name);
```

## アイコンの取得

```java
PackageManager pm = context.getPackageManager();
ActivityInfo activityInfo = resolveInfo.activityInfo;
Drawable icon = activityInfo.loadIcon(pm);
```

## アプリ名の取得

```java
PackageManager pm = context.getPackageManager();
ActivityInfo activityInfo = resolveInfo.activityInfo;
String name = activityInfo.loadLabel(pm);
```

## Activity一覧のソート

プリセットでは表示名でのソートしかなさそう。
昇順/降順の指定はできない。

```java
PackageManager pm = context.getPackageManager();
Collections.sort(resolveInfos, new ResolveInfo.DisplayNameComparator(pm);
```
