Test Driven Development

Ian Cooper:
* The reason to test is a new behavior, not a method on a class.
* Write dirty code to get green, then refactor.
* No new tests for refactored internals and privates (methods and classes).
* Both Develop and Accept again tests written on a port.
* Add Integration tests for coverage of ports to adapters.
* Add system tests for end-to-end confidence.
* Don't mock internals, privates, or adapters.

Alt:
* There’s a behaviour (defined by the API) associated with the system (system under test, SUT). I want to use code to prove that this behaviour exists and is intact. Testing for what we want to preserve between implementations (including aspects of system architecture).
* TDD is a process of discovery.
* New behaviour -> new test (given, when, then). Based on a user story, what is the most obvious next step to moving toward securing the behaviour in that story.
* Tests should test behaviors of a whole system, not individual classes or methods.
* Alternatively -- tests should test the boundaries of a system, not its internals.
* "Unit" test means the test is isolated (produces no side effects and can be run in isolation); not that the code under test is isolated from other code.
* The test suite should be runnable as one without any one test impacting another; NOT each language structure (e.g. a class) must be tested in isolation from other language structures i.e. he unit of isolation is the test, not the thing under test.
* No new unit tests should be written in the "refactor" step (in "red/green/refactor"), because behavior should not be changing at this point.
* Refactoring is the key step for identifying and separating system behaviours and internals.
* In general, people write too many tests against implementation details. Such tests are fragile and have poor (negative?) ROI.
* The bulk of testing should be done in unit tests. Manual/UI/integration tests should be fewer because they do not test business logic at all.
* If you must test implementation details, be willing to write throwaway tests (that you actually throw away once done).
* Sinfully red-green-refactor. Refactoring is the implementation.
* Mocks are for isolating tests, mitigating fragility (as from third party dependencies), and speed (tests can be run in parallel on the same dummy DB). Not isolating the SUT’s dependencies.
* TDD is FAST BINARY FEEDBACK on design decisions. This must fit your use case.

1. Developers write developer tests (“not” unit tests)
2. The trigger for a new test is a new behaviour
3. Customers spicify (not write) aceptance tests
4. Only write production code in response to a test
5. Not all of our code should be driven by TDD


“Dependency is the key problm in software at all scales.” ~ Kent Beck



Defect localisation is emergent of the process. Add-test-work-trst-work-test



