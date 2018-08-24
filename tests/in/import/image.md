// provide default values
[_i_width]=90%
[_b_size]=1px
[_b_type]=solid
[img-border-style]=border:[{{_b_size}}] [{{_b_type}}];padding:1em;
[img-inline-style]=margin-left:auto;margin-right:auto;width:[{{_i_width}}];
[img-st-inline]=[{{img-inline-style}}]
[img-st-inline-border]=[{{img-inline-style}}][{{img-border-style}}]
[img-st-block]=display:block;[{{img-inline-style}}]
[img-st-block-border]=display:block;[img-inline-style][img-border-style]

[img-src-block]=[{{img-src-init}}] [{{img-st-block}}]
[img-src-block-border]=[{{img-src-init}}] [{{img-st-block-border}}]

[img-src-inline]=[{{img-st-inline}}]
[img-src-inline-border]=[{{img-st-inline-border}}]

// These are used to wrap an image in an extras DIV.
[!img-extras]=<div class="extras">[{{img-src-block}}]</div>
[!img-extras-border]=<div class="extras">[{{img-src-block-border}}]</div>

// These are used to put image in 'av' DIV, but w/o dropping a bookmark
[!img-av-block-left]=<div class="av"><ul><li>[{{img-src-block}}]</li></ul><p>[{{ishot}}]</p></div>
[!img-av-block-border-left]=<div class="av"><ul><li>[{{img-src-block-border}}]</li></ul><p>[{{ishot}}]</p></div>
[!img-av-block-right]=<div class="av"><ul><li>[{{ishot}}]</li></ul><p>[{{img-src-block}}]</p></div>
[!img-av-block-border-right]=<div class="av"><ul><li>[{{ishot}}]</li></ul><p>[{{img-src-block-border}}]</p></div>

[!img-av-block-left-desc]=<div class="av"><ul><li>[{{ishot}}]<br /><br /></li><li>[{{img-src-block}}]</li></ul><p>[{{idesc}}]</p></div>
[!img-av-block-border-left-desc]=<div class="av"><ul><li>[{{ishot}}]<br /><br /></li><li>[{{img-src-block-border}}]</li></ul><p>[{{idesc}}]</p></div>

@import "$/imagesize.md"