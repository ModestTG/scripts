package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strconv"
	"strings"

	"github.com/barasher/go-exiftool"
)

func main() {
	filename := os.Args[1]
	et, err := exiftool.NewExiftool()
	if err != nil {
		fmt.Printf("Error when initializing: %v\n", err)
		return
	}
	defer et.Close()
	fmt.Printf("Filename: %v\n", filepath.Base(filename))

	original := et.ExtractMetadata(filename)
	// PrintData(original)
	origDate, err := original[0].GetString("DateTimeOriginal")
	if err != nil {
		fmt.Println(err)
		fmt.Println("Original Datetime: <blank>")
	} else {
		fmt.Printf("Original Datetime: %v\n", origDate)
	}
	original[0].SetString("DateTimeOriginal", ShiftDate(filename))
	et.WriteMetadata(original)
	newDate, err := original[0].GetString("DateTimeOriginal")
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Printf("New Datetime: %v\n\n", newDate)
	}
	// PrintData(original)
}

func PrintData(fileInfo []exiftool.FileMetadata) {
	for _, info := range fileInfo {
		if info.Err != nil {
			fmt.Printf("Error concerning %v: %v\n", info.File, info.Err)
			continue
		}
		for k, v := range info.Fields {
			fmt.Printf("[%v] %v\n", k, v)
		}
	}
}

func ShiftDate(f string) string {
	file := strings.Split(f, "/")
	filename := file[len(file)-1]
	fields := strings.Split(filename, "_")

	dateChars := []rune(fields[0])
	timeChars := []rune(fields[1])

	year := string(dateChars[:4])
	month := string(dateChars[4:6])
	day, _ := strconv.Atoi(string(dateChars[6:]))

	hour, _ := strconv.Atoi(string(timeChars[:2]))
	minute := string(timeChars[2:4])
	second := string(timeChars[4:])

	if hour-6 < 0 {
		hour += 18
		day -= 1
	} else {
		hour -= 6
	}

	date := year + ":" + month + ":" + strconv.Itoa(day)
	time := strconv.Itoa(hour) + ":" + minute + ":" + second
	return date + " " + time
}
