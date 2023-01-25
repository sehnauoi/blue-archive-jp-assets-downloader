# blue-archive-jp-assets-downloader
Assets downloader for Blue Archive (ブルーアーカイブ), a small project that downloads all assets of Blue Archive (JP Version) .

## 先决库

```bash
python3 -m pip install requests
```

## 执行

```bash
python3 ./download_assets.py
```

### 全部跳过时的提示

```pwsh
$ python .\download_assets.py
...
2023-01-25 11:49:19,149 - __main__.<module> - INFO - Script finished.
2023-01-25 11:49:19,149 - __main__.<module> - INFO - Bundle: 3027 total, 0 downloaded, 3027 skipped.
2023-01-25 11:49:19,149 - __main__.<module> - INFO - Media: 11251 total, 0 downloaded, 11251 skipped.
```

### 服务器维护时 (资源不可达) 可能会有的提示

```pwsh
$ python .\download_assets.py
2023-01-24 16:08:28,133 - __main__.<module> - INFO - Current version assets base url (AddressablesCatalogUrlRoot): https://prod-clientpatch.bluearchiveyostar.com/r52_1_27_uulekwyjhzir122lpbrw_2
2023-01-24 16:08:28,403 - root.<module> - WARNING - Provided AddressablesCatalog (https://prod-clientpatch.bluearchiveyostar.com/r52_1_27_uulekwyjhzir122lpbrw_2/Android/) is not accessible at this time.
2023-01-24 16:08:28,605 - root.<module> - WARNING - Provided MediaCatalog (https://prod-clientpatch.bluearchiveyostar.com/r52_1_27_uulekwyjhzir122lpbrw_2/MediaResources/) is not accessible at this time.
2023-01-24 16:08:28,605 - root.<module> - INFO - Script finished.
```

## 存储

`ba_jp_bundles` 文件夹是 Unity Bundle (AssetBundles?)

`ba_jp_media` 文件夹是媒体文件（过场 CG，音乐等）

## 辅助工具

### 下载日服 APK

`download_latest_apk.py`: 从 QooApp 下载其最新版本，并与官方做比照。修改自 [Blue-Archive---Asset-Downloader](https://github.com/K0lb3/Blue-Archive---Asset-Downloader)

```bash
> $ python3 ./download_latest_apk.py                                                                                                                      
Online version: 1.26.183658
Downliading latest apk from QooApp
Downloaded version: 1.26.183658
Unity version used: 2021.3.12f1
```

### 解包 assets

* `extract_bundles.py`: 解包由此下载脚本下载的 bundles，并默认存储于 `extract_bundles` 文件夹。需要 `UnityPy==1.7.21`。建议在 Linux 环境下运行（WSL 也可以）。从 `UnityPy` [样例](https://github.com/K0lb3/UnityPy#example)修改而来

* 默认解包 `Texture2D`，`Sprite`，`TextAsset`。这些类型的资源足够运行（包里的）Spine 动画

```bash
> $ python3 ./extract_bundles.py                                                                                                                      
```

## 💈

嘿嘿 爱丽丝 嘿嘿

我可爱的爱丽丝闺女 嘿嘿 没有你我可怎么活啊

对于体操服优香，我的评价是四个字：好有感觉。我主要想注重于两点，来阐述我对于体操服优香的拙见：第一，我非常喜欢优香。优香的立绘虽然把优香作为好母亲的一面展现了出来（安产型的臀部）。但是她这个头发，尤其是双马尾，看起来有点奇怪。但是这个羁绊剧情里的优香，马尾非常的自然，看上去比较长，真的好棒，好有感觉。这个泛红的脸颊，迷离的眼神，和这个袖口与手套之间露出的白皙手腕，我就不多说了。第二，我非常喜欢体操服。这是在很久很久之前，在认识优香之前，完完全全的xp使然。然而优香她不仅穿体操服，她还扎单马尾，她还穿外套，她竟然还不好好穿外套，她甚至在脸上贴星星（真的好可爱）。（倒吸一口凉气）我的妈呀，这已经到了仅仅是看一眼都能让人癫狂的程度。然而体操服优香并不实装，她真的只是给你看一眼，哈哈。与其说体操服优香让我很有感觉，不如说体操服优香就是为了我的xp量身定做的。抛开这一切因素，只看性格，优香也是数一数二的好女孩：公私分明，精明能干;但是遇到不擅长的事情也会变得呆呆的。我想和优香一起养一个爱丽丝当女儿，所以想在这里问一下大家，要买怎样的枕头才能做这样的梦呢？优香是越看越可爱的，大家可以不必拘束于这机会上的小粗腿优香，大胆的发现这个又呆又努力的女孩真正的可爱之处。

![image](https://user-images.githubusercontent.com/38759782/214242400-b1b029c0-0676-4466-8570-86d7ae38037a.png)

今天我们物理开始讲磁力了，物理老师说铁，镍，钴一类的东西都能被磁化，我听完就悟了，大彻大悟。
课后我问老师：“老师，是不是钴和镍都可以被磁化？”
老师笑了笑，说：“是的。怎么了？”
我赶忙追问：“那我对爱丽丝的爱是不是也可以被磁化？
老师疑惑了，问为什么？
我笑着，红了眼眶：“因为我对爱丽丝的爱就像铁打造的拖拉机一样，轰轰烈烈哐哐锵锵。

给人一种妈妈😇后留下的天真可爱但不知道发生了什么的女儿学着妈妈😇前的样子哄爸爸开心但是又再次让爸爸想起了妈妈的音容笑貌的感觉😢顺带一提爸爸的设定是因为过度悲伤只能住进疗养院只有每周一可以探视

我大抵是病了，横竖都睡不着，坐起身来点起了一支烟，这悲伤没有由来，黯然看着床头的两个枕头，一个是我的，另一个也是我的。
窗外的人们总执着于寻找另一半，而我向来是不屑于此的，可每每见到行人成双结对时，我的心仍旧燃起一丝希冀，也罢，大抵是秋天到了吧。
我大抵是孤身一人太久了，竟希望有个伴来。
我做文章时，她在一旁翻阅我曾写的文字；我不做文章时，就拉着她的手，端详她温柔的眉眼
未曾饮酒，竟生出几分醉意来
大抵是到了该寻一个姑娘的年纪了，近来夜里冷的厉害，特别是心里，凉的出奇，两床被子面对这寒冬的挑衅，也显得有些许吃力了，或许只有心仪姑娘的照料，才能让我感到温暖罢了
我走在路上，一共4个人，一对是情侣，另一对是我和AL-1S
