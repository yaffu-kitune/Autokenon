package main

import (
	"fmt"

	"github.com/gocolly/colly"
)

func main() {

	c := colly.NewCollector()

	//ここでタイトルを取得
	c.OnHTML("title", func(e *colly.HTMLElement) {
		fmt.Println(e.Text)
	})

	c.Visit("https://example.com/")
}
