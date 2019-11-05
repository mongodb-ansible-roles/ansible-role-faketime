# frozen_string_literal: true

describe command('faketime --version') do
  its('stdout') { should eq "\nfaketime: Version 0.9.7\nFor usage information please use 'faketime --help'.\n" }
  its('exit_status') { should eq 0 }
end
