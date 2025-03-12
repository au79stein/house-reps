package main

import (
	"fmt"
	"log"
	"strings"
	"unicode"

	"github.com/PuerkitoBio/goquery"
)

// Helper function to check if a string is a district number (only digits)
func isDistrictNumberInName(name string) bool {
	// Check if the name contains only numbers (district number should be in the name column)
	for _, char := range name {
		if !unicode.IsDigit(char) && char != ' ' && char != '-' {
			return false
		}
	}
	return true
}

func extractTableRows(doc *goquery.Document) {
	// Find the table with the specific class inside the 'view-content' div
	doc.Find(".view-content table[id^='housegov_reps_by_name-block_default']").Each(func(i int, s *goquery.Selection) {
		if s.Length() == 0 {
			fmt.Println("No tables found!")
			return
		}

		// Iterate through each row in the table
		s.Find("tbody tr").Each(func(i int, row *goquery.Selection) {
			// Check if the row has enough columns (td elements)
			cols := row.Find("td")
			if cols.Length() < 6 {
				fmt.Println("Skipping row with insufficient columns")
				return // Skip rows that don't have enough columns
			}

			// Extract the desired data and trim spaces
			name := strings.TrimSpace(cols.Eq(0).Text())
			district := strings.TrimSpace(cols.Eq(1).Text())
			party := strings.TrimSpace(cols.Eq(2).Text())
			officeRoom := strings.TrimSpace(cols.Eq(3).Text())
			phone := strings.TrimSpace(cols.Eq(4).Text())
			committee := strings.TrimSpace(cols.Eq(5).Text())

			// Filter out rows where the "name" column contains only a district number
			if isDistrictNumberInName(name) {
				return // Skip this row
			}

			// Print the row data in aligned columns
			fmt.Printf("%-30s %-35s %-7s %-15s %-20s %s\n", name, district, party, officeRoom, phone, committee)
		})
	})
}

func main() {
	url := "https://www.house.gov/representatives"

	// Make an HTTP request and load the document
	res, err := goquery.NewDocument(url)
	if err != nil {
		log.Fatal(err)
	}

	// Extract table rows and print the formatted output
	// Print column headers once
	fmt.Printf("%-30s %-35s %-7s %-15s %-20s %s\n", "Name", "District", "Party", "Office Room", "Phone", "Committee")
	fmt.Println("----------------------------------------------------------------------------------------------------------------------------------")

	extractTableRows(res)
}

