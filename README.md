# BooleanSearch

## Usage
```
time python main.py --source source.csv --query query.txt --output output.txt
```

## Strategy
### 1. Build Index
1. Parse each title of source file.
2. Remove special characters & numbers in each title. (e.g. '0-9！「」【】（）〈〉《》？：.'.)
3. Split Each title to "2-gram", "3-gram", and English Term. (e.g. "川普, 美國...".)
4. Save each id list as a string, and use split words to create dictionary index.

Index Sample
```
{
  'Apple': '1,3,6,8,9,10',
  'iphone': '1,6,8,12',
  ...
}
```

### 2. Query
1. Split Each query term & query operator(and, or, not) of query file. (e.g. '川普 and 美國'  => ['川普', 'and', '美國'])
2. Split each id string(e.g. '1,3,6,8,9,10') of query word and convert them to set structure ({1,3,6,8,9,10}).
3. Use (and_, or_, sub) build in method to proccess each id sets.
4. Write query results to output file




### Input
#### 1.Source file
More than 100k titles are included.
- [Sample.csv](https://drive.google.com/file/d/1XT72e3pgWC1yUgHX18hxLlVvt3s8Xi7m/view?usp=sharing)

Source format example:

| 1 | MLB／春訓14.2局未失分 克蕭喜迎30歲生日 |
| - | ------------------------ |
| 2 | iPhone X賣得不好 傳首季產量減半     |
| 3 | 中華日報 - 台達攜手成大研發創新科技      |
|   | …                        |

#### 2.Query file
Each line will correspond to a query. We will prepare the query file later.

Query format example:
```
    MLB and 春訓
    iPhone or MLB
    川普 and 美國
```
### Output
#### Output file (txt)
Each line containing all “title id” in ascending order, in which each will correspond to a title matching the boolean operation. Let each id be separated by comma “,”. If there is no title to meet the query form, output 0 for that line. In output.txt, the number of lines should be equal to the number of lines in query.txt.
### Output
Output format example:
```
1,4,6,40,150
1,2,4,6,40,150,1000
0
```
