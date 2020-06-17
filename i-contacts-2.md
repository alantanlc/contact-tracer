# i - Contacts 2

A pandemic has broken out and efforts to perform contact tracing is ongoing. A mobile contact tracing app has been developed, and you are tasked with analyzing the logs. 2 people may meet more than once, but this is still considered as having 1 contact. As entries are added to the log from top to bottom, there will be 1 type of query Q1.

- Q1: For the person(s) who contacted the most people, how many people did he/she contact?
- Q2: How many contact clusters are there, at the point of query?

Number of contact clusters refers to the number of disconnected groups of people. (See image)

![graph](https://s3.amazonaws.com/hr-assets/0/1587123051-1d6ae69d25-Q2.png)

There will be 20 test cases, and the first 10 will only contain Q1 and not Q2. Q1 is easier to solve, and it is recommended that you solve this first.

Q2 is intentionally much harder than Q1, do not worry if you cannot solve it. :)

#### Input Format

- Each line of the log indicates when 2 persons (indicated by phone number M) are in contact wih each other.
- The 2 phone numbers on a line will not be the same.
- The 2 phone numbers on a line will be separated by a single dash.
- There will be a maximum of N lines in the log.
- If a query appears before any contacts are logged, print 0

#### Constraints

1 <= M <= 1,000,000
1 <= N <= 500,000

#### Output Format

An integer every time there is a query.

#### Sample Input 0

```
1-2
Q1
2-3
1-4
5-1
1-5
1-5
Q1
```

#### Sample Output 0

```
1
3
```

#### Explanation 0

On the first query, both person's 1 and 2 have contacted each other, and both have a contact count of 1. Therefore, the highest number of contacts a person has made is 1, and we print 1.

On the second query, person 1 has contacted 3 other people (2, 4, 5), and has the highest contact count. Therefore we print 3.

#### Sample Input 1

```
1-2
Q1
2-3
1-4
5-1
Q1
Q2
6-7
Q2
```

#### Sample Output 1

```
1
3
1
2
```