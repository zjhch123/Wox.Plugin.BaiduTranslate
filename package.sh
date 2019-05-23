rm -rf Translate.wox \
  && rm -rf .DS_Store \
  && zip -r Translate.zip ./ -x '.git/*' \
  && mv Translate.zip Translate.wox