# NOMM Webinar part 2 demo - Securing remote access with SSH Certificates and Hashicorp Vault

In this demo we will show you how to use SSH certificates with EOS and Hashicorp vault.  There are some benefits to using certs instead of copying around ssh keys that most people are used to.

Some benefits:
1. Get rid of having key sprawl, scattering public keys around.  Instead can configure ssh to accept certs that have been signed by your CA

2. Accounting. There is no accountability with respect to managing your SSH keys. You can't manage the lifecycle of access of your systems using SSH. What happens when users leave the company or they leave the team? Do you want them to have access to the instances that they once did? Because, they'll continue to have that as long as they have that PEM key.

3. SSH credentials can have a TTL associated with them. This allows you to auto-revoke those credentials as well. You can set up auditing so that when you access Vault to sign your SSH keys, you can see what's going on in your system. Who's accessing it, what policies they're using, things like that.


Assuming vault is installed and unsealed

1. turn on SSH secrets engine
vault secrets enable -path=ssh-client-signer ssh


2. Configure vault for CA
vault write ssh-client-signer/config/ca generate_signing_key=true

3. Download the public key to the ssh key directory on EOS
DMZ-LF14#copy flash:trusted-user-ca-keys.pem ssh-ca-key:
copy http://10.90.224.172:8200/v1/ssh-client-signer/public_key ssh-ca-key:demo.pem

4. Configure EOS to use public key
management ssh
   trusted-ca key public demo.pem
   ! Note you can also configure revoke lists here too, but may prefer short TTLs

5. Configure user with service principals
username fredlhsu ssh principal netadmin fredlhsu

You can use service principals to provide different levels of access associated with different accounts.  For instance we can assign a rootGlobal principal that gets tied to the root user, only allowing root access to those with rootGlobal to login as root without a password.

username root ssh principal rootGlobal

5. Create a vault role for signing certs

vault write ssh-client-signer/roles/my-role -<<"EOH"
{
  "allow_user_certificates": true,
  "allowed_users": "*",
  "default_extensions": [
    {
      "permit-pty": ""
    }
  ],
  "key_type": "ca",
  "default_user": "arista",
  "ttl": "3m0s"
}
EOH

We could use the allowed_users field to specify what types of users different roles allowed to generate. Also TTL can be set low to automatically revoke the cert after a given time.

6. Have vault sign my public key (assume you've generated a public key on your machine)

vault write -field=signed_key ssh-client-signer/sign/my-role valid_principals="fredlhsu,netadmin"  public_key=@$HOME/.ssh/id_rsa.pub > id_rsa-cert.pub

As an admin you would want to control this process.  Think public cloud.  Using the roles above you can control what types of principals are allowed to be created.

7. Check out the certificate

ssh-keygen -Lf ~/.ssh/id_rsa-cert.pub

8. Change permissions to read only for the public key
chmod 400 .ssh/id_rsa-cert.pub

9. SSH into the switch now without a password

10. For good measure you can remove password auth for the user
username fredlhsu secret *

So now as a standard config for the switches I can put in my username with principals and CA key, without having to put SSH keys in all the configs. With a sufficiently short TTL, these will expire but its not too hard to generate a new one for the user to use.  If they were to leave the cert could be revoked (using EOS CLI), or when TTL expires they would lose access.

