pragma solidity ^0.6.2;


contract KernelStorage {
    // namespace => app id => address
    mapping (bytes32 => mapping (bytes32 => address)) public apps;
    bytes32 public recoveryVaultAppId;
}
