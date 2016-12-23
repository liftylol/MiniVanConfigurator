FROM grahamdumpleton/mod-wsgi-docker:python-3.5-onbuild
RUN apt-get update
RUN apt-get install -y \
  gcc-avr \
  binutils-avr \
  avr-libc \
  dfu-programmer
RUN chown -R www-data /app/tmk_keyboard
RUN chmod -R 774 /app/tmk_keyboard
CMD [ "miniconfig.wsgi" ]
