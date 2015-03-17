# Adapterのレイアウト生成処理の高速化

カスタマイズしたAdapterのレイアウト生成にはInflaterを使って動的に生成することになる。
しかし、毎回Inflaterで生成していると処理が重いので、生成したレイアウトを再利用することにする。

## ViewHolderパターン

レイアウトを再利用すると、中の値まで一緒になってしまうため、値を上書きする必要がある。
その為に毎回Widgetにアクセスするのはコストが高いため、ViewHolderという値クラスを作り**setTag()**で利用する。

```java
private List<ListItem> mItems;
private List<Integer> mCheckedItems;

@Override
public View getView(int position, View convertView, ViewGroup parent)
{
    ViewHolder holder;
    View view = convertView;
    ListItem item = mItems.get(position);
    if (view == null) {
        view = mInflater.inflate(R.layout.item_row, null);
        holder = new ViewHolder();
        holder.title = (TextView)view.findViewById(R.id.title);
        holder.id = (CheckBox)view.findViewById(R.id.id);
        holder.id.setOnCheckedChangeListener(new OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked)
            {
                Integer id = (Integer)buttonView.getTag();
                if (isChecked && !mCheckedItems.contains(id)) {
                    mCheckedItems.add(id);
                } else {
                    mCheckedItems.remove(id);
                }
            }
        });
        view.setTag(holder);
    } else {
        holder = (ViewHolder)view.getTag();
    }

    holder.title.setText(item.getTitle());
    holder.id.setTag(item.getId());
    holder.id.setChecked(mCheckedItems.contains(item.getId()));

    return view;
}

private class ViewHolder
{
    public TextView title;
    public CheckBox id;
}
```
