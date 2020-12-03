package main
import (
    "bufio"
    "fmt"
    "os"
)

func main() {
  first_name := bufio.NewScanner(os.Stdin)
  first_name.Scan()
  fname := first_name.Text()

  second_name := bufio.NewScanner(os.Stdin)
  second_name.Scan()
  lname := second_name.Text()

  age := bufio.NewScanner(os.Stdin)
  age.Scan()
  nage := age.Text()

  town := bufio.NewScanner(os.Stdin)
  town.Scan()
  ltown := town.Text()

  fmt.Println("You are " + fname + " " +lname + " a " + nage + "-years old person from " + ltown + ".")
}
