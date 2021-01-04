# modified from:
# author: Thomas Evangelidis, 2019
# License: BSD-2-Clause

from pymol import cmd, util

def bonds(recsel="clean*", ligsel="vina*", cutoff=3.5):
    """
DESCRIPTION

    Visualize interactions between receptor and ligand.

ARGUMENTS

    recsel = string: atom selection of the receptor {default: "not hetatm"}

    ligsel = string: atom selections of the ligand {default: "hetatm"}

    cutoff = float: show as sticks all receptor residues within this distance from the ligand {default: 5.0}
    """
    cmd.select('ligand', ligsel)
    cmd.select('receptor', recsel)
    cmd.select("pocket", "byres (receptor within %s of ligand and not resn HEM)" % cutoff);
    cmd.show("sticks", "pocket")
    cmd.set('stick_transparency',0.5,'clean*')
    cmd.set('stick_radius',0.05,'clean*')
    cmd.hide('(h. and (e. c extend 1))')
    cmd.set('h_bond_max_angle', 30)
    cmd.set('h_bond_cutoff_center', 3.6)
    cmd.set('h_bond_cutoff_edge', 3.2)
    cmd.dist('ligand_Hbonds', 'ligand', 'receptor', 3.5, mode=2)
    #cmd.dist('pipi','ligand','receptor',2.5,mode=5)
    cmd.set('dash_radius', 0.09)
    # now set the label options
    #cmd.set('label_size', 20)
    #cmd.set('label_position', [0,0,10])

cmd.extend('bonds', bonds)
