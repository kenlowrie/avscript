//@var _id="shot0" \
//     desc="*Short Description*" \
//     lens="**85mm**" \
//     crane="yes" \
//     _format="Shot ID: {{self.name}}[b]Desc: {{self.desc}}[b]Lens:{{self.lens}}[b]"

//[shot0.lens]
//[shot0._format]
//Use 'varv2.' namespace clarifier if needed...
//[varv2.shot0]

[_shotinfo_]=<table class="shotinfo">\
    <tr>\
        <td class="center" colspan="2">***Shot Information***</td>\
    </tr>\
    <tr>\
        <th class="item">Item</th><th class="desc">Description</th>\
    </tr>\
    <tr>\
        <td class="item">Shot</td><td class="desc">{{self._id}}</td>\
    </tr>\
    <tr>\
        <td class="item">Desc</td><td>*{{self.desc}}*</td>\
    </tr>\
    <tr>\
        <td class="item">Lens</td><td>**{{self.lens}}**</td>\
    </tr>\
    <tr>\
        <td class="item">Crane</td><td>{{self.crane}}</td>\
    </tr>\
</table>

//Use _shotinfo_ as _format string
//@var _id="shot1" \
//     desc="*Short Description*" \
//     lens="**85mm**" \
//     crane="yes" \
//     _format="[_shotinfo_]"
//Can be used inside a shot like this
//- WS:a shot
//[var.shot1]
//Or can be used outside a shot like this
//@break
//[var.shot1]
//Use it @raw, except it smashes against the sides...
//@raw [var.shot1]

// Here, you just:
//      [var.shotinfo(shotid="yourshot")]
// on a line by itself will generate the entire shot
@var _id="shotinfo" _format="- [var.{{self.shotid}}.desc]<br />[image.{{self.shotid}}]<br />[var.{{self.shotid}}]" shotid="NOTSET"
@var _id="needshot" _format="- [var.{{self.shotid}}.desc][image.needshot]<br />[var.{{self.shotid}}]" shotid="NOTSET"
