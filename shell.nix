# shell.nix
{ pkgs ? import <nixpkgs> {} }:
let
  gymDuocApp-packages = ps: with ps; [
    django
    cx_oracle
  ];
  GymDuoc = pkgs.python310.withPackages gymDuocApp-packages;
in GymDuoc.env