# First Draft of Flow 


```mermaid
graph TD;
A[Startup Needs] --> B[Job Description]
B --> C[Search]
C --> D{Screen}
D --> |Yes| E[Interview]
D --> |No| F[Reject]
E --> G{Cultural and Technical Fit}
G --> |Yes| H[Offer]
G --> |No| F
```