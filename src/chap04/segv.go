package main

import "fmt"

func main() {
	// nilは必ずページフォールトが発生する
	var p *int = nil
	fmt.Println("不正メモリアクセス前")
	*p = 0
	fmt.Println("不正メモリアクセス後")
}
