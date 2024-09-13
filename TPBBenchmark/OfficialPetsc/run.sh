# /home/bruce/projects/oofem_LCY/build/oofem -f TPB_Xie.in > TPB_Xie.log &
# /home/bruce/projects/oofem_LCY/build/oofem -f TPB_Xie.in -ksp_type cg -pc_type jacobi > TPB_Xie.log &
/home/bruce/Videos/Repo2024/oofem/build/opt/oofem -f TPB_Xie.in -ksp_type cg -pc_type jacobi > TPB_Xie.log &

# python ../visual/extractor.py -f TPB_Xie.in >> ../visual/TPB_4_Petsc.csv