# Historical package fixtures in current validator tests

The validator tests exercise today's command-line implementation against known historical package inputs. They no longer construct an allegedly historical package from the current development checkout.

| Suite | Test file | Fixture commit |
| --- | --- | --- |
| DEAS definition | [test_validate_deas.py](standards/deas/v1/validation/test_validate_deas.py) | `ca8efcefe6568a7a64b5b6d930031dff0131efec` |
| Phase 3 | [test_validate_phase3.py](../contexts/operational-system/docs/program/v1/architecture/phase-3/validation/test_validate_phase3.py) | `f507e927cf98992b7679e46cf536a70fc2fd9c49` |
| Phase 4 | [test_validate_phase4.py](../contexts/operational-system/docs/program/v1/architecture/phase-4/validation/test_validate_phase4.py) | `8f1ccb567af7be41c20452c34ae64c672136e317` |

Each fixture is checked out into an isolated temporary repository from the local Git object database. Missing historical objects cause a setup error; tests do not skip or use current files as fallback. DEAS and Phase 4 retain their committed fixture manifests exactly. Phase 3 places the current validator inside the temporary fixture because its CLI requires that location, then refreshes only the temporary candidate manifest. Its documents still come from the pinned commit. Negative tests mutate disposable copies and retain their expected rejection behavior. Fixture manifests may be recomputed inside negative tests that deliberately isolate semantic checks; repository manifests remain unchanged.

DEAS and Phase 4 invoke the current validator script outside the fixture checkout. Phase 3 invokes the current validator copy inside its fixture. Other historical executable and test files remain manifest-covered package data. A passing test therefore verifies the current validator's behavior on that known package; it does not qualify the current development checkout as the historical package.

The previously failing tests were the DEAS definition positive case, Phase 3 exact-package positive case, and Phase 4's valid-package and clean-committed-package cases. An additional DEAS negative case proves that changing the historical README still fails its manifest check. Current Worker and Observer behavior remains covered by their separate suite against current source.

These tests require full local Git history. Phase 4 also retains an externally pinned historical specification that is not distributed here. Set `DOBEWORKS_PHASE4_SPEC` to an authorized copy with the recorded SHA-256 identity. Without it, the Phase 4 historical tests skip; the current Worker/Observer and benchmark suites remain fully runnable from the public checkout.

## Run

From the repository root:

```sh
python3 -B -m unittest discover -s docs/standards/deas/v1/validation -p 'test_*.py' -v
python3 -B -m unittest discover -s contexts/operational-system/docs/program/v1/architecture/phase-3/validation -p 'test_*.py' -v
python3 -B -m unittest discover -s contexts/operational-system/docs/program/v1/architecture/phase-4/validation -p 'test_*.py' -v
python3 -B -m unittest discover -s contexts/operational-system/software/phase4 -p 'test_*.py' -v
```

The Phase 4 command runs its 32 cases only when `DOBEWORKS_PHASE4_SPEC` names the required historical artifact.
