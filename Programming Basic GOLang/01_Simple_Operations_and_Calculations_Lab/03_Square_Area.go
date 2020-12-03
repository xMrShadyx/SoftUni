package main
import (
    "ioutil"
    "fmt"
    "os"
)

func main() {
  data, err := ioutil.ReadAll(os.Stdin)
  fmt.Println(data, err)
}
