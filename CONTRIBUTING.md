# Contributing

Octopus is a fully public initiative. There is no commercial plan behind it and
there will not be one: no paid tier, no hosted version, no company waiting at
the end. The motivation is simple: everyone should end up with a
superintelligence of their own.

So contributions are open. Any pull request is welcome, and so is any idea.

- **Ideas** go to
  [Discussions](https://github.com/miuuyy/Octopus-SI-OS/discussions/categories/ideas),
  or straight into a pull request if you would rather show than tell.
- **Bugs** go to an [issue](https://github.com/miuuyy/Octopus-SI-OS/issues/new/choose)
  first, then a pull request that references it. The issue is where the
  failure gets reproduced and agreed on before anyone fixes it.

Before filing a bug, work through [TROUBLESHOOTING.md](TROUBLESHOOTING.md).
Never upload a Home, a ledger, provider sign-in files, or unredacted logs.

Octopus was created and is maintained by [@miuuyy](https://github.com/miuuyy).

## Core invariants

- **The kernel stays small and blind.** It knows no provider, channel, tool,
  model, or artifact by name. A branch on a worker pin, a brand, a model
  string, or an artifact label is a bug.
- **Capabilities are descriptors.** If an existing driver or room can express
  it, it is JSON. New executable behavior lives in its owner folder under
  `registry/`.
- **Fail closed.** No silent fallback and no placeholder success. A clear error
  beats something that almost works.
- **Every effect leaves evidence.** It crosses a declared interface under
  policy and is recorded. Marks come from verifiers, never from a model's
  claim.
- Homes, credentials, provider sign-in state, private logs, and absolute user
  paths never enter the repository.

A change that needs a new primitive is still welcome. Open it as an idea first,
because it changes the architecture for everyone.

## Before opening a pull request

Describe the problem, your change, and how you checked it. Run the relevant
[development checks](docs/development.md#checks), and add a regression check
when it can catch the reported failure. State what you did not verify; a local
test, a packaged build, and a real provider reply establish different things.

The PR template's **Architecture fit** section is required only when a proposal
changes architectural responsibilities, contracts, or mechanisms. Read
[Architecture](docs/architecture.md) and the relevant
[contracts](docs/contracts/README.md), then briefly explain why the approach
fits the whole system and why a simpler use of existing primitives is not enough.
An ordinary fix that restores an existing contract does not need this section.

A working implementation is not the only consideration: we also assess whether
the capability belongs in Octopus and whether its approach keeps the architecture
coherent. A useful report can lead to a different fix rather than merging its PR.

## Labels

Maintainers assign labels during the first review; contributors do not need
label permissions to submit. Each issue gets one priority (`P0`–`P3`), and each
PR gets either `urgent` or `non-urgent`. Add `feature` for new capabilities and
`architecture` for architectural changes or questions requiring an architectural
decision. Platform labels are used when the affected platform is known.
Labels describe the work; they do not imply approval or a released fix.
