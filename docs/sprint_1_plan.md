# Sprint 1 plan: load forensic timelines into a database

**Goal:** load the benchmark's timeline CSV files into one SQLite database, with row numbers that match the answer keys.

## Decisions

| Question | Decision |
|---|---|
| Where does the data go? | In 'dataset\', which Git ignores, so the dataset and database are never committed. |
| What if a file has the wrong columns? | Check each file's header as it loads and stop with an error naming the file. |
| What if a timeline is loaded twice? | Replace it's old rows, so there are never duplicates. |
| Keep the original CSV row? | Yes, as an exact copy for the audit trail. |
| What counts as "the same event"? | Same source and message, but a different timestamp description. These rows share a `group_id`. |

**Getting the data:** download the four Zenodo files into `dataset\`.

## The database

- **`events`:** one row per timeline row. It holds the timeline name, row number (counting from 1, header not counted), every CSV column, the original row and a `group_id`.
- **`answer_keys`:** one row per answer-key entry. It holds the timeline name, row number and whether the row is the main or a supporting answer.

## Steps

1. Setup the project
2. Read the CSV file into a list of events
3. Save the sorted events into a SQLite database (to allow look ups of any row by timeline and number) 
4. Add the group IDs
5. Load the answer keys
