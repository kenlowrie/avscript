
// Define some useful variables for substitutions
[lyrics]={:.bigandbold}[{{which}}]
[verse]=<div class="lyrics"><p class="lyrics italic">[{{lyrics}}][{{dblbrk}}][{{lyric}}]</p></div>
[li]=<li style="font-size:1.3em">
[/li]=</li>
[ol]=<div class="extras"><ol style="margin-left:2em">
[/ol]=</ol></div>
[b]=<br />
[dblbrk]=[b][b]
[ul]=<span style="text-decoration:underline">
[/ul]=</span>
[slate]=Title: [title][b]Artist: [artist][b]Directed by: Dan Director[b]Produced by: [link.prodcompany]

[section-class]=:.section
[section]={[{{section-class}}]}--- divTitle
[section-pbb]={[{{section-class}}].pbb}--- divTitle

[scene-class]=:.scene
[scene]={[{{scene-class}}]}--- divTitle


[plain-class]=:.plain
[plain]={[{{plain-class}}]}--- plainTitle
[plain-pbb]={[{{plain-class}}].pbb}--- plainTitle

// probably need to put these in the css file, but for now, this hack is fine.
[wardrobe]={:.wardrobe}**WARDROBE**
[makeup]={:.makeup}**MAKEUP**
[props]={:.props}**PROPS**
[cast]={:.cast}**CAST**

[comment-class]=:.note
[comment]={[{{comment-class}}]}
