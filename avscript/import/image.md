// provide default values

@var _id="img_def" \
      _i_width="90%" \
      _b_size="1px" \
      _b_type="solid" \
      img_border_style="border:{{self._b_size}} {{self._b_type}};padding:1em;" \
      img_inline_style="margin-left:auto;margin-right:auto;width:{{self._i_width}};" \
      img_st_inline="{{self.img_inline_style}}" \
      img_st_inline_border="{{self.img_inline_style}}{{self.img_border_style}}" \
      img_st_block="display:block;{{self.img_inline_style}}" \
      img_st_block_border="display:block;{{self.img_inline_style}}{{self.img_border_style}}" \
      _format="{{self._private_keys_}}{{self._public_keys_}}"

// Some useful defaults for _i_width

[IMG_SIZE_THUMB]=[{{var.img_def._null_(_i_width="20%")}}]
[IMG_SIZE_SMALL]=[{{var.img_def._null_(_i_width="40%")}}]
[IMG_SIZE_MEDIUM]=[{{var.img_def._null_(_i_width="70%")}}]
[IMG_SIZE_LARGE]=[{{var.img_def._null_(_i_width="90%")}}]
