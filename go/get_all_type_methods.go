package main

import (
  "fmt"
  "reflect"
)

type Foo struct {}

func (f Foo) Bar() {
  fmt.Println("Bar")
}

func (f *Foo) Baz() {
  fmt.Println("Baz")
}

func main() {
  fmt.Println("=========Value Refrence Methods=========")
  getMethods(Foo{})

  fmt.Println("=========Pointer Refrence Methods=========")
  getMethods(&Foo{})
}

func getMethods(v interface{}) {
  vType := reflect.TypeOf(v)
  for i := 0; i < vType.NumMethod(); i++ {
      method := vType.Method(i)
      fmt.Println(method.Name)
  }
}

