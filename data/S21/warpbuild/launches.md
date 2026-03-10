# Launches

## WarpBuild: Blazing fast x86-64 and ARM64 runners for Github actions

**WarpBuild provides blazing fast cloud CI runners that speed up of your builds by over 30%.**

This is a drop-in replacement for Github-hosted Actions runners (_including all pre-installed dependencies)_ that takes one line of code change to get started.

Our mission is to deprecate this:

![](https://imgs.xkcd.com/comics/compiling.png)

## **Key benefits:**

Your existing github actions will run without any changes. You will also get:

* **x86-64 and arm** architecture runners
* **30% faster** than GitHub Actions at half the price
* **Secure** VM-level isolation for your workloads
* **Easy debugging** - SSH into running Github actions workflows
* **Fast IO** with SSD backed volumes
* **Unlimited parallelization** for eliminating job queueing delays
* **Automatic updates** of pre-installed toolchains saving maintenance if you are self-hosting runners
* **Runs as a VM**, not in a container, for workloads that don’t work in `dind` or `kind` environments

## **Use cases:**

* **Plain ol’ Github actions**, but faster, cheaper, and awesomer
* **Easy debugging:** ssh into a running workflow using `Action-Debugger`
* **Nested virtualization** for running firecracker, VMs, custom hypervisors, inside of your workflow
* **Running android emulators** in CI
* Spinning up kubernetes clusters in testing pipelines
