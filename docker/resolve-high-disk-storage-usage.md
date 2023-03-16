- CMD to check storage and drill down folder until the cause is found
  `du -cha --max-depth=1 . | grep -E "M|G"`

- In my case I found that /var/lib/docker/containers/<CONTAINER-ID>/<CONTAINER-ID>-json.log was taking up lot of space to solve I ran below cmd
  `truncate -s 0 /var/lib/docker/containers/**/*-json.log`

OR

`find /var/lib/docker/containers/ -type f -iname "*.log" -size +3M -exec truncate -s 0 {} \;`

# CMD to unmount overlay storage
# umount -a --types overlay
