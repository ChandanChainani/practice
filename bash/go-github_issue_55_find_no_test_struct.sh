while read -r line; do
  structName=$(echo $line | cut -d ' ' -f 2)
  fileName=$(echo $line | cut -d ':' -f 1)
  f=$(grep -i $structName"_Marshal" github/*_test.go)
  if [[ -z $f ]]; then
    echo $fileName, $structName
  fi
done < <(
  grep -i 'struct' github/* | grep ":type"
)
