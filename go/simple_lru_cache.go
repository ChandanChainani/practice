package main

import (
	"fmt"
)

type Cache interface {
	Get(key string) (string, bool)
	Set(key, value string) error
}

// in memory cache
// time complexity
// { "108": {"value": "Ambulance", "retrieved": 0}}

type MyCache struct {
	size    int
	counter map[string]int
	store   map[string]string
}

func (m *MyCache) Get(key string) (v string, ok bool) {
	m.counter[key] += 1
	v, ok = m.store[key]
	return
}

func (m *MyCache) Set(key, value string) error {
	if _, ok := m.store[key]; ok {
		return fmt.Errorf("Key already exists")
	}

	if len(m.store) >= m.size {
		min, key := 0, ""
		for k, _ := range m.store {
			if v := m.counter[k]; key == "" || min > v {
				min = v
				key = k
			}
		}
		delete(m.store, key)
	}

	m.store[key] = value

	return nil
}

func NewMyCache(size int) *MyCache {
	return &MyCache{
		size:    size,
		counter: make(map[string]int, size),
		store:   make(map[string]string),
	}
}

func main() {
	var myCache Cache = NewMyCache(3)
	myCache.Set("108", "Ambulance")
	myCache.Set("100", "Police")
	myCache.Set("101", "Theatre")
	myCache.Get("108")
	myCache.Get("101")
	myCache.Get("101")
	myCache.Set("109", "Car")
	fmt.Printf("%#v", myCache)
}
