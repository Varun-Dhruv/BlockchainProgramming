from pymerkle import MerkleTree, verify_inclusion, verify_consistency

transaction_list=[b'a->b->100',
                  b'a->c->50',
                  b'a->d->50',
                  b'b->e->50',
                  b'b->f->50',
                  b'c->g->50',
                  b'c->h->50',
                  b'd->i->50',
                  b'd->j->50',
                  b'e->k->50',
                  b'e->l->50',
                  b'f->m->50',
                  ]
def main():
    tree = MerkleTree()
    # Populate tree with some entries
    for data in transaction_list:
        tree.append_entry(data)

    # Prove and verify inclusion of `bar`
    proof = tree.prove_inclusion(b'e->k->50')
    print(proof)
    verify_inclusion(b'e->k->50', tree.root, proof)

    # Save current state
    sublength = tree.length
    subroot = tree.root

    # Append further entries
    for data in [ b'e->k->50',
                  b'e->l->50',
                  b'f->m->50',]:
        tree.append_entry(data)

    # Prove and verify previous state

    proof = tree.prove_consistency(sublength, subroot)
    print("Proof:", proof)
    verify_consistency(subroot, tree.root, proof)

if __name__=="__main__":
    main()
    