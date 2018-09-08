// Helpers for Shot Generation
@html _id="_table_si_" \
      _inherit="table" \
      class="shotinfo"
@html _id="_td_header_" \
      _inherit="td" \
      class="center" \
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
     _format="{{html._table_si_.<}}\
                {{html.tr.<}}\
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
                    {{html._td_item_.<}}Crane{{html.td.>}}\
                    {{html.td.<}}{{self.crane}}{{html.td.>}}\
                {{html.tr.>}}\
            {{html.table.>}}"

@var _id="_shot_template_" \
     _inherit="_shotinfo2_" \
     desc="{{self.d}}" \
     lens="{{self.l}}" \
     crane="{{self.c}}"
//Would be nice if there was a way to say if {{self.c}} is not defined, make it NO...
@var _id="shot_factory" \
      _format="@var _id=\"{{self.nm}}\" \
      _inherit=\"_shot_template_\" \
      d=\"{{self.d}}\" \
      l=\"{{self.l}}\" \
      c=\"{{self.c}}\" \
     usage="Usage: **{{self.nm}}(d=&quot;desc&quot; l=&quot;lens&quot; c=&quot;crane&quot;)**)" \

@var _id="img_factory" \
      _format="@image _id=\"{{self.nm}}\" src=\"{{self.s}}\" style=\"{{self.st}}\""\
      s="path_to_image"\
      st="[ss]"

@var _id="shotinfo2" _format="- [var.{{self.shotid}}.desc][b][image.{{self.shotid}}][b][var.{{self.shotid}}]" shotid="NOTSET"

// TEMPORARY UNTIL I CONVERT EVERYTHING
@import '$/old_shot.md'
