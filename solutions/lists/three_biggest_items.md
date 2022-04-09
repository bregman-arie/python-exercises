## Three Biggest Items

1. Print three biggest items of a list

### Solution

```python
sorted(some_list, reverse=True)[:3]
```

Or

```python
some_list.sort(reverse=True)
some_list[:3]
```
