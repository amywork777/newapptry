# Rollback Instructions

## Backend Migration Rollback Plan

### What was changed:
1. Updated `.dev.env` API_BASE_URL from `https://api.omiapi.com/` to `https://taya-backend-production.up.railway.app/`
2. Updated `setup.sh` API_BASE_URL variable on line 57

### Files backed up:
- `.dev.env.backup` - Original environment file

### To rollback:

#### Option 1: Use backup file
```bash
cp .dev.env.backup .dev.env
git checkout setup.sh
```

#### Option 2: Manual revert
```bash
# Edit .dev.env and change:
API_BASE_URL=https://taya-backend-production.up.railway.app/
# Back to:
API_BASE_URL=https://api.omiapi.com/

# Edit setup.sh line 57 and change:
API_BASE_URL=https://taya-backend-production.up.railway.app/
# Back to:
API_BASE_URL=https://api.omiapi.com/
```

#### Option 3: If environment code generation needed
```bash
# After reverting files above, regenerate environment files:
dart run build_runner build
# OR run the setup script:
bash setup.sh ios
```

### Verification after rollback:
- Check that app connects to the original backend
- Verify authentication still works
- Test core functionality

### Current status:
- Backend Railway deployment: ✅ WORKING at https://taya-backend-production.up.railway.app/
- Environment files updated: ✅ DONE
- Code generation: ⚠️ PENDING (need Flutter/Dart tools)

### Next steps if rollback needed:
1. Use rollback method above
2. Test app functionality
3. Decide whether to retry migration or stay with original backend