// Helpers for Shot Generation
@html _id="_table_si_" \
      _inherit="table" \
      class="shotinfo"
@html _id="_td_header_" \
      _inherit="td" \
      class="center" \
      colspan="2"
@html _id="_td_2span_" \
      _inherit="td" \
      colspan="2"
@html _id="_td_item_" \
      _inherit="td" \
      class="item" 
@html _id="_td_desc_" \
      _inherit="td" \
      class="item" 
@html _id="_th_item_" \
      _tag="th"\
      _inherit="_td_item_"
@html _id="_th_desc_" \
      _tag="th"\
      _inherit="_td_desc_" 

@var _id="_shotinfo2_" \
     _format="{{html._table_si_.<}}{{self._basic_}}{{html.table.>}}"\
     _notes_="{{html._table_si_.<}}{{self._basic_}}{{self._n_row_}}{{html.table.>}}"\
     _basic_="{{html.tr.<}}\
                {{html._td_header_.<}}***Shot Information***{{html.td.>}}\
              {{html.tr.>}}\
              {{html.tr.<}}\
                {{html._th_item_.<}}Item{{html.th.>}}\
                {{html._th_desc_.<}}Description{{html.th.>}}\
              {{html.tr.>}}\
              {{html.tr.<}}\
                {{html._td_item_.<}}Shot{{html.td.>}}\
                {{html._td_desc_.<}}{{self._id}}{{html.td.>}}\
              {{html.tr.>}}\
              {{html.tr.<}}\
                {{html._td_item_.<}}Desc{{html.td.>}}\
                {{html.td.<}}*{{self.desc}}*{{html.td.>}}\
              {{html.tr.>}}\
              {{html.tr.<}}\
                {{html._td_item_.<}}Lens{{html.td.>}}\
                {{html.td.<}}**{{self.lens}}**{{html.td.>}}\
              {{html.tr.>}}\
              {{html.tr.<}}\
                {{html._td_item_.<}}f-stop{{html.td.>}}\
                {{html.td.<}}**{{self.fstop}}**{{html.td.>}}\
              {{html.tr.>}}\
              {{html.tr.<}}\
                {{html._td_item_.<}}ISO{{html.td.>}}\
                {{html.td.<}}**{{self.iso}}**{{html.td.>}}\
              {{html.tr.>}}\
              {{html.tr.<}}\
                {{html._td_item_.<}}Height{{html.td.>}}\
                {{html.td.<}}**{{self.height}}**{{html.td.>}}\
              {{html.tr.>}}\
              {{html.tr.<}}\
                {{html._td_item_.<}}Crane{{html.td.>}}\
                {{html.td.<}}{{self.crane}}{{html.td.>}}\
              {{html.tr.>}}"\
     _n_row_="{{html.tr.<}}\
                {{html._td_2span_.<}}{{self.notes}}{{html.td.>}}\
              {{html.tr.>}}"

@var _id="_shot_defs_" \
     desc="Your shot description here." \
     lens="24mm" \
     fstop="f/2.8" \
     iso="320" \
     height="36in" \
     crane="No" \
     notes="" \
     val="***default note text***"\
     _format="<strong><em>{{self._}}</em> defaults:</strong>[bb]{{code.split_as(t=\"{{self._public_attrs_}}\")}}"

@var _id="_shot_template_" \
     _inherit="_shotinfo2_" \
     desc="{{code.get_default(v=\"self.d\", default=\"{{var._shot_defs_.desc}}\")}}" \
     lens="{{code.get_default(v=\"self.l\", default=\"{{var._shot_defs_.lens}}\")}}" \
     fstop="{{code.get_default(v=\"self.f\", default=\"{{var._shot_defs_.fstop}}\")}}" \
     iso="{{code.get_default(v=\"self.i\", default=\"{{var._shot_defs_.iso}}\")}}" \
     height="{{code.get_default(v=\"self.h\", default=\"{{var._shot_defs_.height}}\")}}" \
     crane="{{code.get_default(v=\"self.c\", default=\"{{var._shot_defs_.crane}}\")}}"\
     notes="{{code.get_default(v=\"self.n\", default=\"{{var._shot_defs_.notes}}\")}}"\
     addNote="{{code.append(_var_=\"self.notes\", _txtvar_=\"self.val\")}}"\
     addBB="{{self.addNote(val=\"{{bb}}\")}}"\
     val="{{var._shot_defs_.notes}}"\
     usage="Usage: **{{self._}}(d=&quot;desc&quot; l=&quot;lens&quot; c=&quot;crane&quot;)**)"\

@code _id="shot_factory" type="eval" \
    src="print('@var _id=\"$.nm\" _inherit=\"_shot_template_\" \
                     d=\"$.d\" \
                     l=\"$.l\" \
                     f=\"$.f\" \
                     i=\"$.i\" \
                     h=\"$.h\" \
                     c=\"$.c\" \
                     notes=\"$.notes\" \
    ')"\
    d = "{{var._shot_defs_.desc}}" \
    l = "{{var._shot_defs_.lens}}" \
    f = "{{var._shot_defs_.fstop}}" \
    i = "{{var._shot_defs_.iso}}" \
    h = "{{var._shot_defs_.height}}" \
    c = "{{var._shot_defs_.crane}}" \
    notes = "{{var._shot_defs_.notes}}" \
    usage="Usage: **{{self.nm}}(d=&quot;desc&quot; l=&quot;lens&quot; c=&quot;crane&quot;)**)"\

@var _id="img_factory" \
      _format="@image _id=\"{{self.nm}}\" src=\"{{self.s}}\" style=\"{{self.st}}\""\
      s="path_to_image"\
      st="[ss]"

@var _id="shotinfo2" _format="- [var.{{self.shotid}}.desc][b][image.{{self.shotid}}][b][var.{{self.shotid}}]" shotid="NOTSET"
@var _id="needshot" \
     _format="- [var.{{self.shotid}}.desc][image.needshot]<br />[var.{{self.shotid}}]" shotid="NOTSET"

//[imagestyle]=@set _=\"image.$.shotid\" style=\"[{{ss}}]\"
//[storyneeds]=@@ [{{avwrapper.start}}][image.needshot][{{avwrapper.endul}}]
//[storyboard]=@@ [{{avwrapper.start}}][image.$.shotid][{{avwrapper.endul}}]
//[shotdetail]=@@ {{html.p.<}}[var.$.shotid._notes_]{{html.p.>}}[{{avwrapper.enddiv}}]
//[shot_split]=[{{imagestyle}}]\n[{{storyboard}}]\n[{{shotdetail}}]
//[ns_split]=[{{imagestyle}}]\n[{{storyneeds}}]\n[{{shotdetail}}]
//
//[storyneeds2]=@@ [{{avwrapper.start}}][image.needshot][var.$.shotid][{{avwrapper.endul}}]
//[storyboard2]=@@ [{{avwrapper.start}}][image.$.shotid][var.$.shotid][{{avwrapper.endul}}]
//[shotdetail2]=@@ {{html.p.<}}[var.$.shotid.notes]{{html.p.>}}[{{avwrapper.enddiv}}]
//[shot_left]=[{{imagestyle}}]\n[{{storyboard2}}]\n[{{shotdetail2}}]
//[ns_left]=[{{imagestyle}}]\n[{{storyneeds2}}]\n[{{shotdetail2}}]

@var _id="shot_formatter" \
        imagestyle="@set _=\"image.$.shotid\" style=\"{{ss}}\""\
        storyneeds="@@ {{avwrapper.start}}{{image.needshot}}{{avwrapper.endul}}"\
        storyboard="@@ {{avwrapper.start}}{{image.$.shotid}}{{avwrapper.endul}}"\
        shotdetail="@@ {{html.p.<}}{{var.$.shotid._notes_}}{{html.p.>}}{{avwrapper.enddiv}}"\
        storyneeds2="@@ {{avwrapper.start}}{{image.needshot}}{{var.$.shotid}}{{avwrapper.endul}}"\
        storyboard2="@@ {{avwrapper.start}}{{image.$.shotid}}{{var.$.shotid}}{{avwrapper.endul}}"\
        shotdetail2="@@ {{html.p.<}}{{var.$.shotid.notes}}{{html.p.>}}{{avwrapper.enddiv}}"

@var _id="shot_emitter" \
        shot_split="{{var.shot_formatter.imagestyle}}\n{{var.shot_formatter.storyboard}}\n{{var.shot_formatter.shotdetail}}"\
        ns_split="{{var.shot_formatter.imagestyle}}\n{{var.shot_formatter.storyneeds}}\n{{var.shot_formatter.shotdetail}}"\
        shot_left="{{var.shot_formatter.imagestyle}}\n{{var.shot_formatter.storyboard2}}\n{{var.shot_formatter.shotdetail2}}"\
        ns_left="{{var.shot_formatter.imagestyle}}\n{{var.shot_formatter.storyneeds2}}\n{{var.shot_formatter.shotdetail2}}"

@var _id="display" \
    print="0"\
    test="1"\ 
    _format="{{code.equals(v1=\"self.print\", v2=\"self.test\", true=\"self.true\", false=\"self.false\")}}"\
    true="[code.replace(var=\"$.shotid\", val=\"var.display.shotid\", str=\"var.display.push\")]"\
    push="[code.pushlines(shotid=\"$.shotid\" t=\"{{var.shot_emitter.shot_left}}\")]"\
    false=""



//# Example of using code.pushlines to generate
//[code.pushlines(shotid="shot1", t="[storyboard]\n@@ <p>[var.$.shotid]</p>")] 
//[code.pushlines(shotid="shot2a", t="[storyboard]\n[shotdetail]")] 
//[code.pushlines(shotid="shot1", t="[storyboard]\n[shotdetail]")] 
//[code.pushlines(shotid="shot1", t="[shot_split]")] 
